use crate::helpers::period::Period;
use serde;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
pub struct Properties {
    pub periods: Vec<Period>,
}
