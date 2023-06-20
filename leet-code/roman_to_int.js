export function romanToInt(numeral) {
  const translation = {
    I: 1,
    V: 5,
    X: 10,
  };

  const letters = numeral.split('');

  let acc = 0;

  letters.forEach((e, i, a) => {
    if (translation[e] > translation[a[i - 1]]) {
      acc = translation[e] - acc;
    } else {
      acc = acc + translation[e];
    }
  });

  return acc;
}
