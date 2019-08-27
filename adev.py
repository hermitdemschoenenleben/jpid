import allantools
from matplotlib import pyplot as plt
import seaborn as sns

curves = {
    'locked p=0.1 i=0.1': (
        'jakub_locked_p=0.1_i=0.1_10k0Hz.txt',
        'jakub_locked_p=0.1_i=0.1_10kHz.txt',
        'jakub_locked_p=0.1_i=0.1_1kHz.txt',
        'jakub_locked_p=0.1_i=0.1_100Hz.txt',
    ),
    'not locked': (
        'jakub_notlocked_10k0Hz.txt',
        'jakub_notlocked_10kHz.txt',
        'jakub_notlocked_1kHz.txt',
    ),
    # 'locked p=0.025 i=0.05': (
    #     'jakub_locked_p=0.025_i=0.05_10k0Hz.txt',
    # ),
    # 'locked p=0.005 i=0.05': (
    #     'jakub_locked_p=0.005_i=0.05_10k0Hz.txt',
    # ),
    # 'locked p=0.0001 i=0.05': (
    #     'jakub_locked_p=0.0001_i=0.05_10k0Hz.txt',
    # ),
    # 'locked p=0 i=0': (
    #     'jakub_locked_p=0_i=0_10k0Hz.txt',
    # ),
    # 'output zero': (
    #     'jakub_locked_0_10k0Hz.txt',
    # ),
    'new': (
        # 'jakub_p=0.0025_i=0.005_10k0Hz.txt',
        # 'jakub_p=0.0025_i=0.005_LF_10k0Hz.txt',
        # 'jakub_p=0.025_i=0.005_10k0Hz.txt',
        # 'jakub_p=0.0025_i=0.025_10k0Hz.txt',
        'jakub_p=0.0025_i=0.001_10k0Hz.txt',
        'jakub_p=0.0025_i=0.00025_10k0Hz.txt',
    ),
    'new2': (
        'jakub_p=0.0025_i=0.001_d=0.005_10k0Hz.txt',
    )
}


def read_file(fn):
    with open(fn, 'r') as f:
        data = list(f.readlines())[1:]

    data = [
        [
            float(c) for c in
            l.strip().split('\t')
        ]
        for l in data
    ]
    times = [d[0] for d in data]
    frequencies = [d[1] for d in data]
    return times, frequencies

for curve_idx, [label, fns] in enumerate(curves.items()):
    for i_file, fn in enumerate(fns):
        times, frequencies = read_file(fn)
        dt = times[1] - times[0]
        samplerate = 1/dt
        (t2, ad, ade, adn) = allantools.oadev(
            frequencies,
            rate=samplerate,
            data_type="freq",
        )
        kwargs = {}
        if i_file == 0:
            kwargs['label'] = label
        plt.loglog(t2, ad, color=sns.color_palette()[curve_idx], **kwargs)


plt.legend()
plt.show()
