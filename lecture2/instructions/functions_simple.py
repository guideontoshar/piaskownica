def times(x,y):
    """Calculate product of arguments
    """
    return x*y


print(times(2,3))

def density(mass, volume):
    """Calculate object density
    """
    return mass/volume

r = density(23, 8)
rho = density(volume=24.0, mass=12.0)
print("ρ = %f" % (rho,))
