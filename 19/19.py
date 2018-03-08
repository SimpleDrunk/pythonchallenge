# http://www.pythonchallenge.com/pc/hex/bin.html
# butter fly


# import base64
#
# text = open('./19att.txt', 'r').read()
# indian = open('indian.wav', 'wb')
# wav = base64.b64decode(text)
# indian.write(wav)
# indian.close()

import wave

wi = wave.open('indian.wav', 'rb')
wo = wave.open('indian_out.wav', 'wb')
wo.setparams(wi.getparams())
for i in range(wi.getnframes()):
    wo.writeframes(wi.readframes(1)[::-1])
wi.close()
wo.close()
