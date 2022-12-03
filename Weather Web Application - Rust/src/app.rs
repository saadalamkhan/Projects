use crate::components::period_element::PeriodElement;
use crate::helpers::forecast::Forecast;
use js_sys::JsString;
use reqwasm::http::Request;
use web_sys::console;
use yew::functional::*;
use yew::prelude::*;
use yew_router::prelude::*;

/// Helper struct that makes it easier to work with information
/// about a city. Data can be used in
/// https://api.weather.gov/gridpoints/self.office/self.grid_x,self.grid_y/forecast
struct CityInfo {
    pub display_name: String,
    pub office: String,
    pub grid_x: f32,
    pub grid_y: f32,
}

/// Enumeration of all page entries
/// This is convenient because YEW framework focuses only on SPAs (Single Page Application)
#[derive(Debug, Clone, Copy, PartialEq, Routable)]
enum PageEntries {
    #[at("/")]
    ListOfCities,
    #[at("/newyorkcity")]
    NewYorkCity,
    #[at("/losangeles")]
    LosAngeles,
    #[at("/chicago")]
    Chicago,
    #[at("/houston")]
    Houston,
    #[at("/phoenix")]
    Phoenix,
    #[at("/philadelphia")]
    Philadelphia,
    #[at("/sanantonio")]
    SanAntonio,
    #[at("/sandiego")]
    SanDiego,
    #[at("/dallas")]
    Dallas,
    #[at("/sanjose")]
    SanJose,
    #[not_found]
    #[at("/404")]
    NotFound,
}

/// Defines values that will be used to retrieve data from API endpoint
fn get_city_info(city: PageEntries) -> CityInfo {
    match city {
        PageEntries::NewYorkCity => CityInfo {
            display_name: "New York City, NY".to_string(),
            office: "OKX".to_string(),
            grid_x: 24.0,
            grid_y: 32.0,
        },
        PageEntries::LosAngeles => CityInfo {
            display_name: "Los Angeles, CA".to_string(),
            office: "LOX".to_string(),
            grid_x: 154.0,
            grid_y: 44.0,
        },
        PageEntries::Chicago => CityInfo {
            display_name: "Chicago, IL".to_string(),
            office: "LOT".to_string(),
            grid_x: 74.0,
            grid_y: 74.0,
        },
        PageEntries::Houston => CityInfo {
            display_name: "Houston, TX".to_string(),
            office: "HGX".to_string(),
            grid_x: 42.0,
            grid_y: 99.0,
        },
        PageEntries::Phoenix => CityInfo {
            display_name: "Phoenix, AZ".to_string(),
            office: "PSR".to_string(),
            grid_x: 137.0,
            grid_y: 66.0,
        },
        PageEntries::Philadelphia => CityInfo {
            display_name: "Philadelphia, PA".to_string(),
            office: "PHI".to_string(),
            grid_x: 45.0,
            grid_y: 77.0,
        },
        PageEntries::SanAntonio => CityInfo {
            display_name: "San Antonio, TX".to_string(),
            office: "EWX".to_string(),
            grid_x: 113.0,
            grid_y: 68.0,
        },
        PageEntries::SanDiego => CityInfo {
            display_name: "San Diego, CA".to_string(),
            office: "SGX".to_string(),
            grid_x: 56.0,
            grid_y: 13.0,
        },
        PageEntries::Dallas => CityInfo {
            display_name: "Dallas, TX".to_string(),
            office: "FWD".to_string(),
            grid_x: 80.0,
            grid_y: 105.0,
        },
        PageEntries::SanJose => CityInfo {
            display_name: "San Jose, CA".to_string(),
            office: "MTR".to_string(),
            grid_x: 97.0,
            grid_y: 81.0,
        },
        _ => panic!("This shouldn't happen"),
    }
}

/// Returns an HTML element containing a list of each supported city
#[function_component(ListOfCities)]
fn list_of_cities() -> Html {
    html! {
        <>
        <Link<PageEntries> to={PageEntries::NewYorkCity}>{ get_city_info(PageEntries::NewYorkCity).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::LosAngeles}>{ get_city_info(PageEntries::LosAngeles).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::Chicago}>{ get_city_info(PageEntries::Chicago).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::Houston}>{ get_city_info(PageEntries::Houston).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::Phoenix}>{ get_city_info(PageEntries::Phoenix).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::Philadelphia}>{ get_city_info(PageEntries::Philadelphia).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::SanAntonio}>{ get_city_info(PageEntries::SanAntonio).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::SanDiego}>{ get_city_info(PageEntries::SanDiego).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::Dallas}>{ get_city_info(PageEntries::Dallas).display_name }</Link<PageEntries>><br/>
        <Link<PageEntries> to={PageEntries::SanJose}>{ get_city_info(PageEntries::SanJose).display_name }</Link<PageEntries>><br/>
        </>
    }
}

// This uses <a href> HTML element instead of a button
// fn get_weather_page(city: PageEntries) -> Html {
//     let city_info = get_city_info(city);
//     html! {
//         <div>
//             <h1 class="city-name">{ city_info.display_name.to_owned() }</h1>
//             // The following line adds a home button
//             <Link<PageEntries> to={PageEntries::ListOfCities}>{ "Back to the list" }</Link<PageEntries>>
//             <br/>
//             {get_weather(city_info)}
//         </div>
//     }
// }

/// Generic function that handles city generation
fn get_weather_page(city: PageEntries) -> Html {
    let city_info = get_city_info(city);
    let history = use_history().unwrap();
    let go_home = Callback::from(move |_| history.push(PageEntries::ListOfCities));
    html! {
        <div>
            <h1 class="city-name">{ city_info.display_name.to_owned() }</h1>
            <button onclick={go_home} class="return-home-button">{ "Back to the list" }</button>
            <br/>
            {get_weather(city_info)}
        </div>
    }
}

// Handling of individual cities follows

#[function_component(NewYorkCity)]
fn new_york_city() -> Html {
    get_weather_page(PageEntries::NewYorkCity)
}

#[function_component(LosAngeles)]
fn los_angeles() -> Html {
    get_weather_page(PageEntries::LosAngeles)
}

#[function_component(Chicago)]
fn chicago() -> Html {
    get_weather_page(PageEntries::Chicago)
}

#[function_component(Houston)]
fn houston() -> Html {
    get_weather_page(PageEntries::Houston)
}

#[function_component(Phoenix)]
fn phoenix() -> Html {
    get_weather_page(PageEntries::Phoenix)
}

#[function_component(Philadelphia)]
fn philadelphia() -> Html {
    get_weather_page(PageEntries::Philadelphia)
}

#[function_component(SanAntonio)]
fn san_antonio() -> Html {
    get_weather_page(PageEntries::SanAntonio)
}

#[function_component(SanDiego)]
fn san_diego() -> Html {
    get_weather_page(PageEntries::SanDiego)
}

#[function_component(Dallas)]
fn dallas() -> Html {
    get_weather_page(PageEntries::Dallas)
}

#[function_component(SanJose)]
fn san_jose() -> Html {
    get_weather_page(PageEntries::SanJose)
}

#[function_component(App)]
pub fn app() -> Html {
    html! {
        <>
        <h1>{"Saad's Weather Application"}</h1>
        <p>{"Select a city to see its 7 day forecast."}</p>
        <BrowserRouter>
            <Switch<PageEntries> render={Switch::render(switch)} />
        </BrowserRouter>
        </>
    }
}

/// This function was inspired by official docs.rs of yew-router crate.
/// Handles rendering of different page entries, e.g localhost:8080/newyorkcity
fn switch(routes: &PageEntries) -> Html {
    match routes {
        PageEntries::ListOfCities => {
            html! { <ListOfCities /> }
        }
        PageEntries::NewYorkCity => html! {
            <NewYorkCity />
        },
        PageEntries::LosAngeles => html! {
            <LosAngeles />
        },
        PageEntries::Chicago => html! {
            <Chicago />
        },
        PageEntries::Houston => html! {
            <Houston />
        },
        PageEntries::Phoenix => html! {
            <Phoenix />
        },
        PageEntries::Philadelphia => html! {
            <Philadelphia />
        },
        PageEntries::SanAntonio => html! {
            <SanAntonio />
        },
        PageEntries::SanDiego => html! {
            <SanDiego />
        },
        PageEntries::Dallas => html! {
            <Dallas />
        },
        PageEntries::SanJose => html! {
            <SanJose />
        },
        PageEntries::NotFound => html! { <h1>{ "Page not found" }</h1> },
    }
}

/// Here, the actual fetching via API endpoint happens
fn get_weather(city_info: CityInfo) -> Html {
    let weather_forecast = use_state(|| None);
    let weather_forecast_copy = weather_forecast.clone();

    wasm_bindgen_futures::spawn_local(async move {
        let weather_endpoint = format!(
            "https://api.weather.gov/gridpoints/{}/{},{}/forecast",
            city_info.office, city_info.grid_x, city_info.grid_y
        );
        let fetched_weather: Forecast = Request::get(&weather_endpoint)
            .send()
            .await
            .unwrap()
            .json()
            .await
            .unwrap();
        console::log_1(&JsString::from(
            serde_json::to_string(&fetched_weather).unwrap(),
        ));
        weather_forecast.set(Some(fetched_weather));
    });

    match weather_forecast_copy.as_ref() {
        Some(forecast) => forecast
            .properties
            .periods
            .iter()
            .map(|period| {
                html! {
                    <PeriodElement period={period.clone()}/>
                }
            })
            .collect(),
        None => html!({ "No  Data Yet" }),
    }
}
