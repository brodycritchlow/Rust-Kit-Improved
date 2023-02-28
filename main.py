import rustkit
from typing import Any

a = rustkit.Vector()[Any] 
a.push(1); a.push(2); a.push("bool")

print(*a.iter().Py_Iter())