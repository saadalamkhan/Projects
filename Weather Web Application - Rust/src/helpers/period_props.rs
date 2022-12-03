use crate::helpers::period::Period;
use yew::Properties;

#[derive(PartialEq, Properties)]
pub struct PeriodProps {
    pub period: Period,
}
