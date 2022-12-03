use crate::helpers::period_props::PeriodProps;
use yew::prelude::*;

#[function_component(PeriodElement)]
pub fn period_element(props: &PeriodProps) -> Html {
    let PeriodProps { period } = props;
    html! {
        <div class="period">
            <div class="name">{period.name.to_owned()}</div>
            <div class="temp">{period.temperature.to_owned()}{period.temperature_unit.to_owned()}</div>
            <div class="forecast">{period.short_forecast.to_owned()}</div>
            <img src={period.icon.to_owned()}/>
        </div>
    }
}
