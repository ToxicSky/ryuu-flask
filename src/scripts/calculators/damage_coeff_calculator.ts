import axios, { AxiosRequestConfig, AxiosPromise } from 'axios';

class DamageCoeffCalculator
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

export default DamageCoeffCalculator;