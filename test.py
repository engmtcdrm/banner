from proem import Proem

p = Proem(app_nm = 'test-app', flavor_text='this is my flavor', version='v1.0.0')

print(p.build())
print(p._find_max_width())
