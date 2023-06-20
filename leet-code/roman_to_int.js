export function romanToInt(numeral) {
  const translation = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  const letters = numeral.split('');

  let acc = 0;

  letters.forEach((e, i, a) => {
    if (translation[e] > translation[a[i - 1]]) {
      acc = acc + (translation[e] - 2 * translation[a[i - 1]]);
    } else {
      acc = acc + translation[e];
    }
  });

  return acc;
}
