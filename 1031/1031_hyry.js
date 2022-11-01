// 1. 50000번 100000번 비교할 일 자체를 없애자 (e.g. if문)
// 2. sort도 미리 해 놓는 것이 낫다
// score의 범위가 넓지만,
// 언어, 직무, 연차, 음식은 3 * 2 * 2 * 2 로 낮은 경우의 수
// => 이러한 경우의 수도 미리 만들어 두자

const re = / and | /g;

const getPossibleKeys = (_lan, _pos, _lvl, _food) => {
  const keys = [];

  for (const lan of [_lan, "-"]) {
    for (const pos of [_pos, "-"]) {
      for (const lvl of [_lvl, "-"]) {
        for (const food of [_food, "-"]) {
          keys.push(lan + pos + lvl + food);
        }
      }
    }
  }

  return keys;
};

const initializeKeys = () => {
  const infoDic = {};

  const lanType = ["cpp", "java", "python", "-"];
  const posType = ["frontend", "backend", "-"];
  const lvlType = ["junior", "senior", "-"];
  const foodType = ["chicken", "pizza", "-"];

  for (const lan of lanType) {
    for (const pos of posType) {
      for (const lvl of lvlType) {
        for (const food of foodType) {
          infoDic[lan + pos + lvl + food] = [];
        }
      }
    }
  }
  
  return infoDic;
};

const makeInfoDic = (info) => {
  const infoDic = initializeKeys();

  for (const userInfo of info) {
    const [lan, pos, lvl, food, _score] = userInfo.split(re);
    const score = Number(_score);
    const keys = getPossibleKeys(lan, pos, lvl, food);

    for (const key of keys) {
      infoDic[key].push(score);
    }
  }

  for (key in infoDic) {
    infoDic[key].sort((a, b) => a - b);
  }

  return infoDic;
};

const binarySearch = (scoreArr, minScore) => {
  let left = 0;
  let right = scoreArr.length - 1;
  let ans = right + 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (scoreArr[mid] >= minScore) {
      right = mid - 1;
      ans = Math.min(ans, mid);
    } else {
      left = mid + 1;
    }
  }

  return ans;
};

function solution(info, query) {
  const answer = [];
  const infoDic = makeInfoDic(info);

  for (const eachQuery of query) {
    const [lan, pos, lvl, food, minScore] = eachQuery.split(re);
    const key = lan + pos + lvl + food;

    let tmpSum = 0;
    // const scoreArr = infoDic[key].sort((a, b) => a - b);
    const scoreArr = infoDic[key];
    const ans = binarySearch(scoreArr, +minScore);
    tmpSum += scoreArr.length - ans;

    answer.push(tmpSum);
  }

  return answer;
}
