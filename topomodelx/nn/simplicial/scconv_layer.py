"""Simplicial 2-complex convolutional neural network."""
import torch

from topomodelx.base.aggregation import Aggregation
from topomodelx.base.conv import Conv


class SCConvLayer(torch.nn.Module):
    """Layer of a Simplicial 2-complex convolutional neural network (SCConv).

    Implementation of the SCConv layer proposed in [ERIC20]_.



    References
    ----------
    .. [ERIC20] Bunch, Eric, Qian You, Glenn Fung, and Vikas Singh.
        Simplicial 2-complex convolutional neural nets.
        NeurIPS 2020 Workshop TDA and Beyond homepage
        https://openreview.net/forum?id=TLbnsKrt6J-

    """

    def __init__(
            self,
            channels,
    ):
        super().__init__()

    def reset_parameters(self):
        r"""reset parameters."""

    def forward(self):
        r"""Forward pass."""
