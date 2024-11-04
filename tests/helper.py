import os
<<<<<<< HEAD

from facefusion.filesystem import create_directory, is_directory, is_file, remove_directory
from facefusion.temp_helper import get_base_directory_path
=======
import tempfile

from facefusion.filesystem import create_directory, is_directory, is_file, remove_directory
>>>>>>> upstream/feat/ui-indicator
from facefusion.typing import JobStatus


def is_test_job_file(file_path : str, job_status : JobStatus) -> bool:
	return is_file(get_test_job_file(file_path, job_status))


def get_test_job_file(file_path : str, job_status : JobStatus) -> str:
	return os.path.join(get_test_jobs_directory(), job_status, file_path)


def get_test_jobs_directory() -> str:
<<<<<<< HEAD
	return os.path.join(get_base_directory_path(), 'test-jobs')
=======
	return os.path.join(tempfile.gettempdir(), 'facefusion-test-jobs')
>>>>>>> upstream/feat/ui-indicator


def get_test_example_file(file_path : str) -> str:
	return os.path.join(get_test_examples_directory(), file_path)


def get_test_examples_directory() -> str:
<<<<<<< HEAD
	return os.path.join(get_base_directory_path(), 'test-examples')
=======
	return os.path.join(tempfile.gettempdir(), 'facefusion-test-examples')
>>>>>>> upstream/feat/ui-indicator


def is_test_output_file(file_path : str) -> bool:
	return is_file(get_test_output_file(file_path))


def get_test_output_file(file_path : str) -> str:
	return os.path.join(get_test_outputs_directory(), file_path)


def get_test_outputs_directory() -> str:
<<<<<<< HEAD
	return os.path.join(get_base_directory_path(), 'test-outputs')
=======
	return os.path.join(tempfile.gettempdir(), 'facefusion-test-outputs')
>>>>>>> upstream/feat/ui-indicator


def prepare_test_output_directory() -> bool:
	test_outputs_directory = get_test_outputs_directory()
	remove_directory(test_outputs_directory)
	create_directory(test_outputs_directory)
	return is_directory(test_outputs_directory)
