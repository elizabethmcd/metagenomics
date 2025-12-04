# This file is auto-generated, PLEASE DO NOT EDIT DIRECTLY! To update, run
#
#   $ latch generate-metadata --nextflow nextflow_schema.json
#
# Add any custom logic or parameters in `latch_metadata/__init__.py`.

import typing
from dataclasses import dataclass, field
from enum import Enum

import typing_extensions
from flytekit.core.annotation import FlyteAnnotation

from latch.ldata.path import LPath
from latch.types.directory import LatchDir
from latch.types.file import LatchFile
from latch.types.metadata import Params, Section, Spoiler, Text
from latch.types.samplesheet_item import SamplesheetItem



@dataclass
class NextflowSchemaArgsType:
    input: typing_extensions.Annotated[LatchFile, FlyteAnnotation({'display_name': 'Input', 'default': None, 'samplesheet': False, 'output': False, 'required': True, 'description': 'Path to comma-separated file containing information about the samples in the experiment.'})]
    outdir: typing_extensions.Annotated[LatchDir, FlyteAnnotation({'display_name': 'Outdir', 'default': None, 'samplesheet': False, 'output': True, 'required': True, 'description': 'The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.'})]
    platform: typing_extensions.Annotated[str, FlyteAnnotation({'display_name': 'Platform', 'default': None, 'samplesheet': False, 'output': False, 'required': True})]
    single_end: typing_extensions.Annotated[typing.Optional[bool], FlyteAnnotation({'display_name': 'Single End', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    sourmash_dbs: typing_extensions.Annotated[typing.Optional[LatchFile], FlyteAnnotation({'display_name': 'Sourmash Dbs', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    diamond_db: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Diamond Db', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    multiqc_config: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Multiqc Config', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    multiqc_title: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Multiqc Title', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    multiqc_logo: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Multiqc Logo', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    multiqc_methods_description: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Multiqc Methods Description', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    email: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Email', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    email_on_fail: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Email On Fail', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    plaintext_email: typing_extensions.Annotated[typing.Optional[bool], FlyteAnnotation({'display_name': 'Plaintext Email', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    monochrome_logs: typing_extensions.Annotated[typing.Optional[bool], FlyteAnnotation({'display_name': 'Monochrome Logs', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    hook_url: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Hook Url', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    show_hidden_params: typing_extensions.Annotated[typing.Optional[bool], FlyteAnnotation({'display_name': 'Show Hidden Params', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    enable_conda: typing_extensions.Annotated[typing.Optional[bool], FlyteAnnotation({'display_name': 'Enable Conda', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    config_profile_description: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Config Profile Description', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    config_profile_contact: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Config Profile Contact', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    config_profile_name: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Config Profile Name', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    config_profile_url: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Config Profile Url', 'default': None, 'samplesheet': False, 'output': False, 'required': False})]
    diamond_columns: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Diamond Columns', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore')
    validate_params: typing_extensions.Annotated[typing.Optional[bool], FlyteAnnotation({'display_name': 'Validate Params', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'boolean': True}}}, 'type': {'simple': 'BOOLEAN', 'structure': {'tag': 'bool'}}}}}, 'samplesheet': False, 'output': False, 'required': False, 'description': 'Boolean whether to validate parameters against the schema at runtime'})] = field(default=True)
    max_multiqc_email_size: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Max Multiqc Email Size', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': '25.MB'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='25.MB')
    tracedir: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Tracedir', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': 'null/pipeline_info'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='null/pipeline_info')
    publish_dir_mode: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Publish Dir Mode', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': 'copy'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='copy')
    schema_ignore_params: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Schema Ignore Params', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': 'config_profile_name,config_profile_url,config_profile_contact,config_profile_description,custom_config_base,custom_config_version,enable_conda,genomes,hook_url'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='config_profile_name,config_profile_url,config_profile_contact,config_profile_description,custom_config_base,custom_config_version,enable_conda,genomes,hook_url')
    custom_config_version: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Custom Config Version', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': 'master'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='master')
    custom_config_base: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Custom Config Base', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': 'https://raw.githubusercontent.com/nf-core/configs/master'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='https://raw.githubusercontent.com/nf-core/configs/master')
    max_memory: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Max Memory', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': '400.GB'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='400.GB')
    max_time: typing_extensions.Annotated[typing.Optional[str], FlyteAnnotation({'display_name': 'Max Time', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'stringValue': '240.h'}}}, 'type': {'simple': 'STRING', 'structure': {'tag': 'str'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default='240.h')
    max_cpus: typing_extensions.Annotated[typing.Optional[int], FlyteAnnotation({'display_name': 'Max Cpus', 'default': {'scalar': {'union': {'value': {'scalar': {'primitive': {'integer': '16'}}}, 'type': {'simple': 'INTEGER', 'structure': {'tag': 'int'}}}}}, 'samplesheet': False, 'output': False, 'required': False})] = field(default=16)





generated_flow = [Section('Input/output options', Text('Define where the pipeline should find input data and save output data.'), Params('input', 'outdir', 'platform'), Spoiler('Optional Parameters', Params('single_end', 'sourmash_dbs', 'diamond_db', 'diamond_columns'))), Spoiler('Generic options', Text('Less common options for the pipeline, typically set in a config file.'), Params('validate_params', 'multiqc_config', 'multiqc_title', 'multiqc_logo', 'max_multiqc_email_size', 'multiqc_methods_description', 'tracedir', 'publish_dir_mode', 'email', 'email_on_fail', 'plaintext_email', 'monochrome_logs', 'hook_url', 'schema_ignore_params', 'show_hidden_params', 'enable_conda', 'custom_config_version', 'custom_config_base', 'config_profile_description', 'config_profile_contact', 'config_profile_name', 'config_profile_url')), Spoiler('Max job request options', Text('Set the top limit for requested resources for any single job'), Params('max_memory', 'max_time', 'max_cpus'))]
