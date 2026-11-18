# Evaluate a polynomial efficiently: implementation

## What the example does

Horner evaluation uses one multiply and add per coefficient. Coefficients are ordered from highest degree to the constant term.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "coefficients": [
    2,
    3,
    4
  ],
  "x": 2
}
```

Expected result:

```json
18
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
