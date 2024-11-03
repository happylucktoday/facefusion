from typing import Optional

import gradio

from facefusion import state_manager
from facefusion.execution import detect_execution_devices
from facefusion.typing import ExecutionDevice

VIDEO_MEMORY_INDICATOR_HTML : gradio.HTML
VIDEO_UTILIZATION_INDICATOR_HTML : gradio.HTML


def render() -> None:
	global VIDEO_MEMORY_INDICATOR_HTML
	global VIDEO_UTILIZATION_INDICATOR_HTML

	if get_execution_device():
		with gradio.Row():
			VIDEO_MEMORY_INDICATOR_HTML = gradio.HTML(
				value = create_video_memory_indicator_html,
				every = 2
			)


def get_execution_device() -> Optional[ExecutionDevice]:
	execution_device_id = int(state_manager.get_item('execution_device_id'))
	execution_devices = detect_execution_devices()

	return execution_devices[execution_device_id]


def create_video_memory_indicator_html() -> str:
	video_memory = get_execution_device().get('memory')
	return '<progress class="progress-indicator" max="' + str(video_memory.get('total').get('value')) + '" value="' + str(video_memory.get('total').get('value') - video_memory.get('free').get('value')) + '"></progress>'
