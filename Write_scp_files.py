import os
from pathlib import Path
## -------------------------------------  Train -----------------------------------------------

SNR_all = [0, 5]
Noise_type_all = ['Babble', 'Car']
Audio_sample = 10
maindir = 'F:/Speech Enhancement Projects'
rootdir = 'F:/Speech Enhancement Projects' + '/Database/Original_Samples/'
Path(os.path.dirname(maindir +'/scpfiles/')).mkdir(parents=True, exist_ok=True)
file = open(maindir  +'/scpfiles/Train.txt','w')

for Noise_type in Noise_type_all:
    for SNR in SNR_all:
        for i in range(Audio_sample):
            signal_path = rootdir + '/Train/Clean/Clean_' + str(i + 1) + '.wav'
            noisy_path = rootdir + '/Train/Noisy/Noisy_' + Noise_type + '_' + str(SNR) + '_dB_' + str(i + 1) + '.wav'
            L = noisy_path + " - " + signal_path
            file.writelines(L)
            file.write('\n')
file.close()

# ##-------------------------------------  Dev ------------------------------------------------------

SNR_all = [0, 5]
Noise_type_all = ['Babble', 'Car']
Audio_sample = 5
sample_margin = 11  # As number of train sample was 10

file = open(maindir  +'/scpfiles/Dev.txt','w')
for Noise_type in Noise_type_all:
    for SNR in SNR_all:
        for i in range(Audio_sample):
            signal_path = rootdir + '/Dev/Clean/Clean_' + str(i + sample_margin) + '.wav'
            noisy_path = rootdir + '/Dev/Noisy/Noisy_' + Noise_type + '_' + str(SNR) + '_dB_' + str(i + sample_margin) + '.wav'
            L = noisy_path + " - " + signal_path
            file.writelines(L)
            file.write('\n')
file.close()

## -------------------------------------  Eval -----------------------------------------------------

SNR_all = [0, 5]
Noise_type_all  = ['Babble', 'Car']
Audio_sample = 5
file = open(maindir  +'/scpfiles/Test.txt','w')
sample_margin = 16

for Noise_type in Noise_type_all:
    for SNR in SNR_all:
        for i in range(Audio_sample):
            Enhanced_path = rootdir + '/Test/Enhanced/Enhanced_' + Noise_type + '_' + str(SNR) + '_dB_' + str(i + sample_margin) + '.wav'
            signal_path = rootdir + '/Test/Clean/Clean_' + str(i + sample_margin) + '.wav'
            noisy_path = rootdir + '/Test/Noisy/Noisy_' + Noise_type + '_' + str(SNR) + '_dB_' + str(i+sample_margin) + '.wav'
            L = noisy_path + " - " + signal_path + " " + Enhanced_path
            file.writelines(L)
            file.write('\n')
file.close()
