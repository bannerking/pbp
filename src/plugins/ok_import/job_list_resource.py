from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob
from open_karelia_import import openKareliaImport
from job_list_resource_factory import JobListResourceFactory

JobListResource = JobListResourceFactory(
    OKImportParser, ThreadJob, openKareliaImport)
