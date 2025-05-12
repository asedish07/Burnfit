# 5/3/1 프로그램 데이터셋 생성기

import random
import json

def calculate_531_weights(one_rm):
  tm = one_rm * 0.9
  schedule = {
    "1주차": [0.65, 0.75, 0.85],
    "2주차": [0.70, 0.80, 0.90],
    "3주차": [0.75, 0.85, 0.95]
  }
  result = {}
  for week, percents in schedule.items():
    result[week] = [round(tm * p / 2.5) * 2.5 for p in percents]  # 2.5kg 단위 반올림
  return result

def generate_entry():
  # 무작위 1RM 설정
  squat = random.randint(80, 200)
  bench = random.randint(50, 150)
  deadlift = random.randint(100, 220)
  ohp = random.randint(30, 80)
  days_per_week = random.choice([3, 4, 5])

  input_text = f"1RM: 스쿼트 {squat}kg, 벤치프레스 {bench}kg, 데드리프트 {deadlift}kg, 오버헤드프레스 {ohp}kg\n주당 운동일수: {days_per_week}일"

  # 프로그램 생성
  programs = {
    "스쿼트": calculate_531_weights(squat),
    "벤치프레스": calculate_531_weights(bench),
    "데드리프트": calculate_531_weights(deadlift),
    "오버헤드프레스": calculate_531_weights(ohp)
  }

  output_text = "당신의 5/3/1 프로그램은 다음과 같습니다:\n"
  for week in ["1주차", "2주차", "3주차"]:
    output_text += f"{week}:\n"
    for lift, values in programs.items():
      if week in values:
        reps = ["5회", "5회", "5+회"] if week == "1주차" else \
               ["3회", "3회", "3+회"] if week == "2주차" else \
               ["5회", "3회", "1+회"]
        sets = ", ".join([f"{values[week][i]}kg {reps[i]}" for i in range(3)])
        output_text += f" - {lift}: {sets}\n"
  return {"input": input_text, "output": output_text.strip()}

# 여러 개 생성
dataset = [generate_entry() for _ in range(400)]

# 저장
with open("prompt_tuning_dataset.json", "w", encoding="utf-8") as f:
  for item in dataset:
    f.write(json.dumps(item, ensure_ascii=False) + "\n")


# jsonl to json 변환

import json

# 원본 jsonl 파일 경로
input_path = "prompt_tuning_dataset.jsonl"
# 변환 후 저장할 json 파일 경로
output_path = "prompt_tuning_dataset.json"

data = []

with open(input_path, "r", encoding="utf-8") as f:
  for line in f:
    data.append(json.loads(line))

# 리스트 전체를 JSON으로 저장
with open(output_path, "w", encoding="utf-8") as f:
  json.dump(data, f, ensure_ascii=False, indent=2)