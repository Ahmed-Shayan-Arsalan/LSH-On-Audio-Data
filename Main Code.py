import os
import pickle
import numpy as np
import librosa
from datasketch import MinHash, MinHashLSH
from pydub import AudioSegment
from pydub.playback import play


num_perm = 128
directory = r"C:\Users\Lenovo\Downloads\drive-download-20230206T184623Z-002"

def mfcc_to_binary(mfccs):
    threshold = np.mean(mfccs)
    binary = np.zeros(mfccs.shape)
    binary[mfccs >= threshold] = 1
    return binary

if os.path.exists('lsh_index.pickle'):
    with open('lsh_index.pickle', 'rb') as f:
        lsh = pickle.load(f)
else:
    lsh = MinHashLSH(threshold=0.9, num_perm=num_perm)

for filename in os.listdir(directory):
    if filename.endswith('.mp3'):
       
        audio, sr = librosa.load(os.path.join(directory, filename))
        
        
        mfcc = librosa.feature.mfcc(audio, sr)
        
        binary_mfcc = mfcc_to_binary(mfcc)
        

        m = MinHash(num_perm=num_perm)
        for i, v in np.ndenumerate(binary_mfcc):
            if v == 1:
                m.update(str(i).encode('utf8'))
        
        if filename not in lsh:
            lsh.insert(filename, m)

            
            with open('lsh_index.pickle', 'wb') as f:
                pickle.dump(lsh, f)

audio, sr = librosa.load("ASSIGNMENT 1\\AudioFiles\\001\\001039.mp3")

   
mfcc1= librosa.feature.mfcc(audio, sr)
        
    
binary_mfcc = mfcc_to_binary(mfcc1)
        
      
mhash = MinHash(num_perm=num_perm)
for i, v in np.ndenumerate(binary_mfcc):
    if v == 1:
        mhash.update(str(i).encode('utf8'))

model = pickle.load(open("lsh.pkl", 'rb'))
result1 = model.query(m)
if len(result1) > 1:
    print( result1)

        
     
