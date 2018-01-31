import DamageCoeffCalculator from './calculators/damage_coeff_calculator';

var calc = new DamageCoeffCalculator();
// console.log(calc);
var damage_coeff_form = document.querySelector('form');
damage_coeff_form.addEventListener('onsubmit', calc.calculate_damage_coeff);
console.log(damage_coeff_form);