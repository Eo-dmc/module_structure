import torch

__all__ = ['TensorCalculator']


class TensorCalculator():
    """A class to perform various operations with PyTorch tensors."""

    def __init__(self):
        """
         Initializes the TensorCalculator class.
        """
        pass

    def tensor_ones(self, dim_x, dim_y, dim_z):
        """
        Returns a tensor filled with ones.

        :param dim_x: The size of the first dimension of the tensor.
        :param dim_y: The size of the second dimension of the tensor.
        :param dim_z: The size of the third dimension of the tensor.
        :return: A tensor filled with ones.
        """
        ones = torch.ones([dim_x, dim_y, dim_z])
        return ones

    def tensor_zeros(self, dim_x, dim_y, dim_z):
        """
        Returns a tensor filled with zeros.

        :param dim_x: The size of the first dimension of the tensor.
        :param dim_y: The size of the second dimension of the tensor.
        :param dim_z: The size of the third dimension of the tensor.
        :return: A tensor filled with zeros.
        """
        zeros = torch.zeros([dim_x, dim_y, dim_z])
        return zeros

    def tensor_random(self, dim_x, dim_y, dim_z):
        """
        Returns a tensor filled with random values.

        :param dim_x: The size of the first dimension of the tensor.
        :param dim_y: The size of the second dimension of the tensor.
        :param dim_z: The size of the third dimension of the tensor.
        :return: A tensor filled with random values.
        """
        random_tensor = torch.rand([dim_x, dim_y, dim_z])
        return random_tensor

    def tensor_sum(self, tensor1, tensor2):
        """
        Returns the sum of two tensors.
        :param tensor1: The first tensor to be added.
        :param tensor2: The second tensor to be added.
        :return: The sum of two sensors.
        """
        if tensor1.size() != tensor2.size():
            raise ValueError("The tensors must have the same dimensions to be added.")
        return tensor1 + tensor2

    def tensor_multiply(self, tensor1, tensor2):
        """
        Returns the product of two tensors element-wise.
        :param tensor1: The first tensor to be multiplied.
        :param tensor2: The second tensor to be multiplied.
        :return: The product of the two tensors element-wise.
        """
        if tensor1.size() != tensor2.size():
            raise ValueError("The tensors must have the same dimensions to be multiplied.")
        return tensor1 * tensor2
