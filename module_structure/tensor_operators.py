import torch

__all__ = ['TensorCalculator']


class TensorCalculator():

    def __init__(self):

        return None

    def tensor_ones(self,
                    dim_x,
                    dim_y,
                    dim_z):
        ones = torch.ones([dim_x, dim_y, dim_z])
        return ones

    def tensor_zeros(self, dim_x, dim_y, dim_z):
        zeros = torch.zeros([dim_x, dim_y, dim_z])
        return zeros

    def tensor_random(self, dim_x, dim_y, dim_z):
        random_tensor = torch.rand([dim_x, dim_y, dim_z])
        return random_tensor

    def tensor_sum(self, tensor1, tensor2):
        if tensor1.size() != tensor2.size():
            raise ValueError("The tensors must have the same dimensions to be added.")
        return tensor1 + tensor2

    def tensor_multiply(self, tensor1, tensor2):
        if tensor1.size() != tensor2.size():
            raise ValueError("The tensors must have the same dimensions to be multiplied.")
        return tensor1 * tensor2
