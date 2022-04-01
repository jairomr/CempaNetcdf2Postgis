from glob impor glob

from cirrus.util.config import settings, logger



from xgrads import CtlDescriptor, open_CtlDataset

def grads_to_tiff():
    downloads_dir = f'{settings.CEMPADIR}downloads'
    files = glob(f'{downloads_dir}/*.ctl')
    BRAMS_data = files[0]
    data1 = open_CtlDataset(BRAMS_data)
    data1