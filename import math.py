import math

def calculate_sphere_volume(radius):
    return (4/3) * math.pi * math.pow(radius, 3)

def calculate_sphere_surface_area(radius):
    return 4 * math.pi * math.pow(radius, 2)

def format_result(radius, volume, surface_area):
    return f"""
{'='*50}
구의 계산 결과
{'='*50}
반지름(r): {radius} cm
부피(V): {volume:.2f} cm³
겉넓이(S): {surface_area:.2f} cm²
{'='*50}
"""
def main():
    print("구의 부피와 겉넓이 계산 프로그램")
    print("-" * 50)
    
    try:
        radius = float(input("구의 반지름을 입력하세요 (cm): "))
        
        if radius <= 0:
            print("반지름은 0보다 큰 값.")
            return
        
        volume = calculate_sphere_volume(radius)
        surface_area = calculate_sphere_surface_area(radius)
        
        result = format_result(radius, volume, surface_area)
        print(result)
        
    except ValueError:
        print("⚠️ 올바른 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()