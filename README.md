# mercurytools

a lightweight and consistent set of data structures designed for clarity, predictability, and ease of use in everyday development. Built to provide a clean, pythonic interface over fundamental data structures, with an emphasis on readability and extensibility rather than abstraction-heavy implementations.

## installation

```bash
# install from PyPI
pip install mercurytools

# development
git clone https://github.com/waltermichelraja/mercurytools.git
pip install -e .
pytest
```

## overview
| structure        | operations |
|:----------------|:-----------|
| LinkedList      | `append`, `prepend`, `insert`, `remove`, `pop` |
| Stack           | `push`, `pop`, `peek` |
| Deque           | `append`, `appendleft`, `pop`, `popleft` |
| utilities       | `extend`, `reverse`, `clear`, `copy`, `to_list` |
| special methods | `__len__`, `__iter__`, `__reversed__`, `__getitem__`, `__contains__`, `__eq__`, `__repr__` |

<br>

***LICENSE:** this project is licensed under the MIT License, checkout [license](https://github.com/waltermichelraja/mercurytools/blob/main/LICENSE) file for further details.*\
***BUG REPORTS:** if you encounter a bug or unexpected behavior, please open an issue in: [issues](https://github.com/waltermichelraja/mercurytools/issues)*
