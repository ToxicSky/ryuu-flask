import DamageCoeffCalculator from './calculators/damage_coeff_calculator';

var calc = new DamageCoeffCalculator();
// console.log(calc);
var damage_coeff_form = document.querySelector('form button');
damage_coeff_form.addEventListener('onclick', calc.calculate_damage_coeff);
console.log(damage_coeff_form);