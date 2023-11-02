import torch

__all__ = ['TensorCalculator']


class TensorCalculator:
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

    # EXTRA FUNCTIONS
    def tensor_identity(self, dim):
        """
        Returns an identity tensor of size dim x dim.

        :param dim: The size of the square identity tensor.
        :return: An identity tensor of size dim x dim.
        """
        identity = torch.eye(dim)
        return identity

    def tensor_ones_like(self, other_tensor):
        """
        Returns a tensor filled with ones of the same size as the provided tensor.

        :param other_tensor: A tensor whose size is used to create the ones tensor.
        :return: A tensor filled with ones of the same size as the input tensor.
        """
        ones_like = torch.ones_like(other_tensor)
        return ones_like

    def tensor_zeros_like(self, other_tensor):
        """
        Returns a tensor filled with zeros of the same size as the provided tensor.

        :param other_tensor: A tensor whose size is used to create the zeros tensor.
        :return: A tensor filled with zeros of the same size as the input tensor.
        """
        zeros_like = torch.zeros_like(other_tensor)
        return zeros_like


# Create an instance of the TensorCalculator class
calculator = TensorCalculator()

# Example 1: Creating tensors filled with ones
ones_tensor = calculator.tensor_ones(2, 3, 4)
print(ones_tensor)

# Example 2: Creating tensors filled with zeros
zeros_tensor = calculator.tensor_zeros(3, 2, 2)
print(zeros_tensor)

# Example 3: Creating tensors filled with random values
random_tensor = calculator.tensor_random(2, 2, 3)
print(random_tensor)

# Example 4: Adding two tensors
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])
sum_result = calculator.tensor_sum(tensor1, tensor2)
print(sum_result)

# Example 5: Multiplying two tensors element-wise
tensor3 = torch.tensor([[1, 2], [3, 4]])
tensor4 = torch.tensor([[5, 6], [7, 8]])
multiply_result = calculator.tensor_multiply(tensor3, tensor4)
print(multiply_result)

# Example 6: Creating an identity tensor
identity_tensor = calculator.tensor_identity(3)
print(identity_tensor)

# Example 7: Creating a tensor filled with ones like another tensor
reference_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
ones_like_tensor = calculator.tensor_ones_like(reference_tensor)
print(ones_like_tensor)

# Example 8: Creating a tensor filled with zeros like another tensor
reference_tensor = torch.tensor([[0.1, 0.2], [0.3, 0.4]])
zeros_like_tensor = calculator.tensor_zeros_like(reference_tensor)
print(zeros_like_tensor)
