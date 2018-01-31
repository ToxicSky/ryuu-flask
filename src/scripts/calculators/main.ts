import axios, { AxiosRequestConfig, AxiosPromise } from 'axios';

class Calculator
{
  public calculate_damage_coeff(e: Event) {
    e.preventDefault();

    axios({
      method: 'post',
      url: '/api/calculators/damage_resistance',

      data: {
        damage: 100,
        damage_resist: 50
      }
    }).then(function(response: any) {
      console.log(response.data);
    });
  }
}

window.calc = new Calculator;
console.log(calc);
var damage_coeff_form = document.querySelector('form');
damage_coeff_form.addEventListener('onsubmit', calc.calculate_damage_coeff);
console.log(damage_coeff_form);