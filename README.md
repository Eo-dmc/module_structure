# TensorCalculator Module

The TensorCalculator module is a Python library that allows you to perform various operations with PyTorch tensors. It provides functions for creating tensors filled with ones, zeros, random values, as well as performing element-wise addition and multiplication. Additionally, it includes extra functions for working with identity tensors, ones-like, and zeros-like tensors.

## Installation

You can install the TensorCalculator module using pip. It requires PyTorch to be installed, so make sure you have PyTorch installed in your Python environment.
Make sure to activate first your environment that includes the requirements.

```bash
pip install -U git+https://github.com/Eo-dmc/module_structure.git
```

## Usage
Here's how you can use the TensorCalculator module:

```bash
import torch
from TensorCalculator import TensorCalculator

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
tensor2 = torch.tensor([[5, 6], [7, 8])
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
```

## Documentation
For detailed information about the available functions and their parameters, please refer to the docstrings in the source code.

## License
This module is distributed under the MIT License. See the LICENSE file for details.

## Support
If you have any questions or need assistance, please contact emigdiodmc@gmail.com.

Enjoy working with tensors using the TensorCalculator module :)!
