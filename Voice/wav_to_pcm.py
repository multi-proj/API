!pip install librosa
import librosa    
y, s = librosa.load('test0202.wav', sr=16000)

import sys
import os.path

file = open('test0202.wav', 'rb')


byteBuffer = bytearray(file.read())

file.close()



fn_ext = os.path.splitext('test0202.wav')

if fn_ext[1] == '.wav':

	out_filename = fn_ext[0] + '.pcm'

else:

	out_filename = fn_ext[0] + fn_ext[1] + '.pcm'

print 'Out file name: %s' % out_filename



out_file = open(out_filename, 'wb')

out_file.write(byteBuffer[44:])

out_file.close()

		

raw_input('Press Enter to exit')

exit(0)
