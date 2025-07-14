import Live
from .AAA_SMC_Mixer import AAA_SMC_Mixer


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return AAA_SMC_Mixer(c_instance)

# local variables:
# tab-width: 4
