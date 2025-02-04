''' auto mixed precision related functions '''
import mindspore as ms
from mindspore.amp import LossScaler

class NoLossScaler(LossScaler):
    """
    No LossScaler
    """
    def scale(self, inputs):
        return inputs

    def unscale(self, inputs):
        return inputs

    def adjust(self, grads_finite):
        return True


