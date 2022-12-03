use crate::helpers::properties::Properties;
use serde;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
pub struct Forecast {
    pub properties: Properties,
}
