# Qiskit 설치가 필요할 경우 주석 해제
# !pip install qiskit

from qiskit import QuantumCircuit, Aer, execute

# 양자 회로 생성
qc = QuantumCircuit(2)
qc.h(0)  # 0번 큐비트에 Hadamard 게이트 적용 -> 중첩 상태로 만듦
qc.cx(0, 1)  # 0번과 1번 큐비트를 얽힘 상태로 만듦
qc.measure_all()  # 모든 큐비트 측정

# 시뮬레이터를 사용하여 양자 회로 실행
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()
counts = result.get_counts()

print("양자 컴퓨터 처리 결과(측정값):", counts)
