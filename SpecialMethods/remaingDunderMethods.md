| **Dunder Method** | **Called By**            | **Purpose**                                           |
| ----------------- | ------------------------ | ----------------------------------------------------- |
| `__repr__`        | `repr(obj)`              | Unambiguous, developer-oriented representation        |
| `__str__`         | `str(obj)`, `print(obj)` | Readable, end user friendly format display            |
| `__eq__`          | `obj1 == obj2`           | Defines equality comparison between objects           |
| `__len__`         | `len(obj)`               | Returns length; also affects truthiness (`bool(obj)`) |
| `__enter__`       | Start of a `with` block  | Acquire resource (context manager setup)              |
| `__exit__`        | End of a `with` block    | Release resource and handle exceptions                |
