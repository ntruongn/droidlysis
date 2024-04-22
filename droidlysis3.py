#!/usr/bin/env python3

"""
__author__ = "Axelle Apvrille"
__license__ = "MIT License"
"""
import argparse
import os
import subprocess
import droidutil  # that's my own utilities
import droidsample
import droidreport
import sys
import logging
from droidsql import DroidSql
from droidconfig import generalconfig

property_dump_file = 'details.md'
report_file = 'report.md'
json_file = 'report.json'
__version__ = "3.4.7"

def process_file(infile,
                 outdir='/tmp/analysis',
                 json_dir = 'jsons',
                 verbose=False,
                 clear=True,
                 disable_report=False,
                 silent=False,
                 no_kit_exception=False,
                 sql=None,
                 disable_json=False,
                 import_exodus=False):
    """Static analysis of a given file"""
    config = generalconfig(filename='conf/general.conf', verbose=True)
    if os.access(infile, os.R_OK):
        if not silent:
            print("Processing file: " + infile + " ...")
        sample = droidsample.droidsample(config=config,
                                         filename=infile,
                                         output=outdir,
                                         verbose=verbose,
                                         clear=clear,
                                         disable_description=disable_report,
                                         silent=silent,
                                         no_kit_exception=no_kit_exception,
                                         import_exodus=import_exodus)
        sample.unzip()
        sample.disassemble()
        sample.extract_file_properties()
        sample.extract_meta_properties()
        # sample.extract_manifest_properties()
        sample.extract_dex_properties()
        listofkits = sample.extract_kit_properties()
        if no_kit_exception:
            listofkits = []
        sample.extract_smali_properties(listofkits)
        sample.extract_wide_properties(listofkits)

        if sql is not None:
            sample.properties.write(sql)

        json_file = os.path.basename(infile).split('.')[0]+'.json'
        if not disable_json:
            os.makedirs(json_dir, exist_ok=True)
            sample.properties.dump_json(os.path.join(json_dir, json_file))

        if not silent and not clear:
            report = droidreport.droidreport(sample, console=True, report_to_file=disable_report)
            report.write(os.path.join(sample.outdir, report_file), verbose)

        if not clear:
            analysis_file = open(os.path.join(sample.outdir, property_dump_file), 'a')
            analysis_file.write(str(sample.properties))
            analysis_file.close()
        else:
            if not silent:
                print("Removing directory %s ..." % (sample.outdir))
            proc = subprocess.Popen(['rm', '-rf', sample.outdir])
            proc.communicate()

        sample.close()


if __name__ == "__main__":
    process_file(sys.argv[1])
