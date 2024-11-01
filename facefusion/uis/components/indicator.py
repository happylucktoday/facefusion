from typing import Optional

import gradio

from facefusion import state_manager
from facefusion.execution import detect_execution_devices
from facefusion.typing import ExecutionDevice

VIDEO_UTILIZATION_INDICATOR_HTML : gradio.HTML
VIDEO_MEMORY_INDICATOR_HTML : gradio.HTML


def render() -> None:
	global VIDEO_UTILIZATION_INDICATOR_HTML
	global VIDEO_MEMORY_INDICATOR_HTML

	if get_execution_device():
		VIDEO_UTILIZATION_INDICATOR_HTML = gradio.HTML(
			label = 'VIDEO_UTILIZATION_INDICATOR', #move to wording.get()
			value = create_video_utilization_html,
			every = 1
		)
		VIDEO_MEMORY_INDICATOR_HTML = gradio.HTML(
			label = 'VIDEO MEMORY INDICATOR', #move to wording.get()
			value = create_video_memory_html,
			every = 1
		)
	# SYSTEM MEMORY INDICATOR


def get_execution_device() -> Optional[ExecutionDevice]:
	execution_device_id = int(state_manager.get_item('execution_device_id'))
	execution_devices = detect_execution_devices()

	return execution_devices[execution_device_id]


def create_video_utilization_html() -> str:
	device_utilization = get_execution_device().get('utilization')
	return '<progress class="progress-indicator" max="100" value="' + str(device_utilization.get('gpu').get('value')) + '"></progress>'


def create_video_memory_html() -> str:
	video_memory = get_execution_device().get('memory')
	return '<progress class="progress-indicator" max="' + str(video_memory.get('total').get('value')) + '" value="' + str(video_memory.get('total').get('value') - video_memory.get('free').get('value')) + '"></progress>'
