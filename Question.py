def product(a=0.0, b=0.0):
    return a * b


print("Coordinates of P:")
px, py = int(input("x: ")), int(input("y: "))
print("Coordinates of Q:")
qx, qy = int(input("x: ")), int(input("y: "))
T = []
M = ((px + qx) / 2.0, (py + qy) / 2.0)

print("Enter Factors:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

T = [a, b, c, d]
PX = product(T[0], px) + product(T[2], py)
PY = product(T[1], px) + product(T[3], py)
QX = product(T[0], qx) + product(T[2], qy)
QY = product(T[1], qx) + product(T[3], qy)
N = ((PX + QX) / 2.0, (PY + QY) / 2.0)
MX = product(T[0], M[0]) + product(T[2], M[1])
MY = product(T[1], M[0]) + product(T[3], M[1])
print(PX, PY)
print(QX, QY)
print(MX, MY)
print(N[0], N[1])


