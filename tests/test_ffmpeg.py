<<<<<<< HEAD
import glob
import subprocess
=======
import subprocess
import tempfile
>>>>>>> upstream/feat/ui-indicator

import pytest

from facefusion import process_manager, state_manager
from facefusion.download import conditional_download
<<<<<<< HEAD
from facefusion.ffmpeg import concat_video, extract_frames, read_audio_buffer
from facefusion.temp_helper import clear_temp_directory, create_temp_directory, get_temp_directory_path
=======
from facefusion.ffmpeg import concat_video, extract_frames, read_audio_buffer, replace_audio, restore_audio
from facefusion.filesystem import copy_file
from facefusion.temp_helper import clear_temp_directory, create_temp_directory, get_temp_file_path, get_temp_frame_paths
>>>>>>> upstream/feat/ui-indicator
from .helper import get_test_example_file, get_test_examples_directory, get_test_output_file, prepare_test_output_directory


@pytest.fixture(scope = 'module', autouse = True)
def before_all() -> None:
	process_manager.start()
	conditional_download(get_test_examples_directory(),
	[
		'https://github.com/facefusion/facefusion-assets/releases/download/examples-3.0.0/source.jpg',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples-3.0.0/source.mp3',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples-3.0.0/target-240p.mp4'
	])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('source.mp3'), get_test_example_file('source.wav') ])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-240p.mp4'), '-vf', 'fps=25', get_test_example_file('target-240p-25fps.mp4') ])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-240p.mp4'), '-vf', 'fps=30', get_test_example_file('target-240p-30fps.mp4') ])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('target-240p.mp4'), '-vf', 'fps=60', get_test_example_file('target-240p-60fps.mp4') ])
<<<<<<< HEAD
	state_manager.init_item('temp_frame_format', 'jpg')
=======
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('source.mp3'), '-i', get_test_example_file('target-240p.mp4'), '-ar', '16000', get_test_example_file('target-240p-16khz.mp4') ])
	subprocess.run([ 'ffmpeg', '-i', get_test_example_file('source.mp3'), '-i', get_test_example_file('target-240p.mp4'), '-ar', '48000', get_test_example_file('target-240p-48khz.mp4') ])
	state_manager.init_item('temp_path', tempfile.gettempdir())
	state_manager.init_item('temp_frame_format', 'png')
>>>>>>> upstream/feat/ui-indicator
	state_manager.init_item('output_audio_encoder', 'aac')


@pytest.fixture(scope = 'function', autouse = True)
def before_each() -> None:
	state_manager.clear_item('trim_frame_start')
	state_manager.clear_item('trim_frame_end')
	prepare_test_output_directory()


def test_extract_frames() -> None:
	target_paths =\
	[
		get_test_example_file('target-240p-25fps.mp4'),
		get_test_example_file('target-240p-30fps.mp4'),
		get_test_example_file('target-240p-60fps.mp4')
	]

	for target_path in target_paths:
<<<<<<< HEAD
		temp_directory_path = get_temp_directory_path(target_path)
		create_temp_directory(target_path)

		assert extract_frames(target_path, '452x240', 30.0) is True
		assert len(glob.glob1(temp_directory_path, '*.jpg')) == 324
=======
		create_temp_directory(target_path)

		assert extract_frames(target_path, '452x240', 30.0) is True
		assert len(get_temp_frame_paths(target_path)) == 324
>>>>>>> upstream/feat/ui-indicator

		clear_temp_directory(target_path)


def test_extract_frames_with_trim_start() -> None:
	state_manager.init_item('trim_frame_start', 224)
<<<<<<< HEAD
	providers =\
=======
	target_paths =\
>>>>>>> upstream/feat/ui-indicator
	[
		(get_test_example_file('target-240p-25fps.mp4'), 55),
		(get_test_example_file('target-240p-30fps.mp4'), 100),
		(get_test_example_file('target-240p-60fps.mp4'), 212)
	]

<<<<<<< HEAD
	for target_path, frame_total in providers:
		temp_directory_path = get_temp_directory_path(target_path)
		create_temp_directory(target_path)

		assert extract_frames(target_path, '452x240', 30.0) is True
		assert len(glob.glob1(temp_directory_path, '*.jpg')) == frame_total
=======
	for target_path, frame_total in target_paths:
		create_temp_directory(target_path)

		assert extract_frames(target_path, '452x240', 30.0) is True
		assert len(get_temp_frame_paths(target_path)) == frame_total
>>>>>>> upstream/feat/ui-indicator

		clear_temp_directory(target_path)


def test_extract_frames_with_trim_start_and_trim_end() -> None:
	state_manager.init_item('trim_frame_start', 124)
	state_manager.init_item('trim_frame_end', 224)
<<<<<<< HEAD
	providers =\
=======
	target_paths =\
>>>>>>> upstream/feat/ui-indicator
	[
		(get_test_example_file('target-240p-25fps.mp4'), 120),
		(get_test_example_file('target-240p-30fps.mp4'), 100),
		(get_test_example_file('target-240p-60fps.mp4'), 50)
	]

<<<<<<< HEAD
	for target_path, frame_total in providers:
		temp_directory_path = get_temp_directory_path(target_path)
		create_temp_directory(target_path)

		assert extract_frames(target_path, '452x240', 30.0) is True
		assert len(glob.glob1(temp_directory_path, '*.jpg')) == frame_total
=======
	for target_path, frame_total in target_paths:
		create_temp_directory(target_path)

		assert extract_frames(target_path, '452x240', 30.0) is True
		assert len(get_temp_frame_paths(target_path)) == frame_total
>>>>>>> upstream/feat/ui-indicator

		clear_temp_directory(target_path)


def test_extract_frames_with_trim_end() -> None:
	state_manager.init_item('trim_frame_end', 100)
<<<<<<< HEAD
	providers =\
=======
	target_paths =\
>>>>>>> upstream/feat/ui-indicator
	[
		(get_test_example_file('target-240p-25fps.mp4'), 120),
		(get_test_example_file('target-240p-30fps.mp4'), 100),
		(get_test_example_file('target-240p-60fps.mp4'), 50)
	]

<<<<<<< HEAD
	for target_path, frame_total in providers:
		temp_directory_path = get_temp_directory_path(target_path)
		create_temp_directory(target_path)

		assert extract_frames(target_path, '426x240', 30.0) is True
		assert len(glob.glob1(temp_directory_path, '*.jpg')) == frame_total
=======
	for target_path, frame_total in target_paths:
		create_temp_directory(target_path)

		assert extract_frames(target_path, '426x240', 30.0) is True
		assert len(get_temp_frame_paths(target_path)) == frame_total
>>>>>>> upstream/feat/ui-indicator

		clear_temp_directory(target_path)


def test_concat_video() -> None:
	output_path = get_test_output_file('test-concat-video.mp4')
	temp_output_paths =\
	[
		get_test_example_file('target-240p.mp4'),
		get_test_example_file('target-240p.mp4')
	]

	assert concat_video(output_path, temp_output_paths) is True


def test_read_audio_buffer() -> None:
	assert isinstance(read_audio_buffer(get_test_example_file('source.mp3'), 1, 1), bytes)
	assert isinstance(read_audio_buffer(get_test_example_file('source.wav'), 1, 1), bytes)
	assert read_audio_buffer(get_test_example_file('invalid.mp3'), 1, 1) is None
<<<<<<< HEAD
=======


def test_restore_audio() -> None:
	target_paths =\
	[
		get_test_example_file('target-240p-16khz.mp4'),
		get_test_example_file('target-240p-48khz.mp4')
	]
	output_path = get_test_output_file('test-restore-audio.mp4')

	for target_path in target_paths:
		create_temp_directory(target_path)
		copy_file(target_path, get_temp_file_path(target_path))

		assert restore_audio(target_path, output_path, 30) is True

		clear_temp_directory(target_path)


def test_replace_audio() -> None:
	target_path = get_test_example_file('target-240p.mp4')
	output_path = get_test_output_file('test-replace-audio.mp4')

	create_temp_directory(target_path)
	copy_file(target_path, get_temp_file_path(target_path))

	assert replace_audio(target_path, get_test_example_file('source.mp3'), output_path) is True
	assert replace_audio(target_path, get_test_example_file('source.wav'), output_path) is True

	clear_temp_directory(target_path)
>>>>>>> upstream/feat/ui-indicator
