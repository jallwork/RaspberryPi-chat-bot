import keys

def wait():	
	import struct
	import pyaudio
	import pvporcupine

	success = False
	porcupine = None
	pa = None
	audio_stream = None

	access_key = keys.key['PORCUPINE_KEY']

	try:
		porcupine = pvporcupine.create(access_key=access_key,keywords=["blueberry"])

		pa = pyaudio.PyAudio()

		audio_stream = pa.open(
			rate=porcupine.sample_rate,
			channels=1,
			format=pyaudio.paInt16,
			input=True,
			frames_per_buffer=porcupine.frame_length)

		while  not success:
			pcm = audio_stream.read(porcupine.frame_length)
			pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

			keyword_index = porcupine.process(pcm)

			if keyword_index >= 0:
				success = True
	finally:
		if porcupine is not None:
			porcupine.delete()

		if audio_stream is not None:
			audio_stream.close()

		if pa is not None:
			pa.terminate()
		return (success)
