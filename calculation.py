import math


def formula_1(target, u=0, v=0, a=0, t=0):
    """v = u + a·t"""
    if target == 'v':
        return u + a * t
    if target == 'u':
        return v - a * t
    if target == 'a':
        if t == 0:
            raise ValueError("Time (t) cannot be zero when solving for a.")
        return (v - u) / t
    if target == 't':
        if a == 0:
            raise ValueError(
                "Acceleration (a) cannot be zero when solving for t."
            )
        return (v - u) / a
    raise ValueError(f"Invalid target: {target}")


def formula_2(target, u=0, v=0, s=0, t=0):
    """s = ((u + v) / 2) · t"""
    if target == 's':
        return 0.5 * (u + v) * t
    if target == 'u':
        if t == 0:
            raise ValueError("Time (t) cannot be zero when solving for u.")
        return (2 * s / t) - v
    if target == 'v':
        if t == 0:
            raise ValueError("Time (t) cannot be zero when solving for v.")
        return (2 * s / t) - u
    if target == 't':
        if (u + v) == 0:
            raise ValueError(
                "Sum of velocities (u + v) cannot be zero when solving for t."
            )
        return (2 * s) / (u + v)
    raise ValueError(f"Invalid target: {target}")


def formula_3(target, u=0,a=0, s=0, t=0):
    """s = u·t + (1/2)·a·t²"""
    if target == 's':
        return u * t + 0.5 * a * t**2
    if target == 'u':
        if t == 0:
            raise ValueError("Time (t) cannot be zero when solving for u.")
        return (s - 0.5 * a * t**2) / t
    if target == 'a':
        if t == 0:
            raise ValueError("Time (t) cannot be zero when solving for a.")
        return 2 * (s - u * t) / (t**2)
    if target == 't':
        if a == 0:
            if u == 0:
                raise ValueError("Cannot solve for t when both a and u are 0.")
            return s / u

        discriminant = u**2 + 2 * a * s
        if discriminant < 0:
            raise ValueError("No real solution for time (t).")

        t1 = (-u + math.sqrt(discriminant)) / a
        t2 = (-u - math.sqrt(discriminant)) / a
        positives = [val for val in (t1, t2) if val >= 0]

        if not positives:
            raise ValueError("No non-negative time solution exists.")
        return min(positives)

    raise ValueError(f"Invalid target: {target}")


def formula_4(target,v=0,a=0,s=0,t=0):
    """s = v·t − ½·a·t²"""
    if target == 's': return v*t - 0.5 *a*(t**2)
    if target == 'v':
        if t == 0: raise ValueError("t cannot be zero")
        return (s+ 0.5 * a * (t**2)) / t
    if target == 'a':
        if t == 0: raise ValueError("t cannot be zero")
        return 2 * (v * t - s) / (t ** 2)
    if target == 't':
        # s = v·t − ½·a·t²  →  −½·a·t² + v·t − s = 0
        A, B, C = -0.5 * a, v, -1*s
        return _quadratic(A, B, C)
    raise ValueError(f"Invalid target: {target}")


def formula_5(target, u=0, v=0, a=0, s=0):
    """v² = u² + 2·a·s"""
    if target == 'v':
        val = u**2 + 2 * a * s
        if val < 0:
            raise ValueError("Resulting v² is negative; no real solution.")
        return math.sqrt(val)
    if target == 'u':
        val = v**2 - 2 * a * s
        if val < 0:
            raise ValueError("Resulting u² is negative; no real solution.")
        return math.sqrt(val)
    if target == 'a':
        if s == 0:
            raise ValueError(
                "Displacement (s) cannot be zero when solving for a."
            )
        return (v**2 - u**2) / (2 * s)
    if target == 's':
        if a == 0:
            raise ValueError(
                "Acceleration (a) cannot be zero when solving for s."
            )
        return (v**2 - u**2) / (2 * a)
    raise ValueError(f"Invalid target: {target}")

def _quadratic(A, B, C):
    """Solve A·x² + B·x + C = 0, return list of real non-negative roots."""
    disc = B * B - 4 * A * C
    if disc < 0:
        return []
    if A == 0:
        return [-C / B] if B != 0 else []
    roots = [(-B + math.sqrt(disc)) / (2 * A),
             (-B - math.sqrt(disc)) / (2 * A)]
    return [r for r in roots if r >= 0]



# FORMULAS = {
#     '1': ("v = u + a·t",            formula_1, "uvat"),
#     '2': ("s = ((u+v)/2)·t",        formula_2, "suvt"),
#     '3': ("s = u·t + ½·a·t²",       formula_3, "suat"),
#     '4': ("s = v·t − ½·a·t²",       formula_4, "svat"),
#     '5': ("v² = u² + 2·a·s",        formula_5, "uvas"),
# }

# def main():
#     print("Available formulas:")
#     for key, (desc, _, vars_) in FORMULAS.items():
#         print(f"  {key}) {desc:<22}  (variables: {', '.join(vars_)})")
#     print()

#     choice = input("Choose a formula (1-5): ").strip()
#     if choice not in FORMULAS:
#         print("Invalid choice.")
#         return

#     desc, func, variables = FORMULAS[choice]
#     print(f"\nUsing: {desc}")
#     print(f"Variables involved: {', '.join(variables)}\n")

#     target = input(f"Which variable to find? ({'/'.join(variables)}): ").strip().lower()
#     if target not in variables:
#         print("Invalid target.")
#         return

#     vals = {}
#     for name in variables:
#         if name == target:
#             continue
#         try:
#             vals[name] = float(input(f"Enter value of {name}: "))
#         except ValueError:
#             print(f"Invalid number for {name}.")
#             return

#     # Compute
#     try:
#         result = func(vals, target)
#     except ValueError as e:
#         print(f"Error: {e}")
#         return

#     if isinstance(result, list):
#         if not result:
#             print("No real non-negative solution.")
#         else:
#             for r in result:
#                 print(f"{target} = {r}")
#     else:
#         print(f"{target} = {result}")


# if __name__ == "__main__":
#     main()
