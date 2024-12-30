let map, marker, autocomplete;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 12.4634, lng: 53.8232 },  // Domyślne centrum (możesz zmienić)
        zoom: 8
    });

    map.addListener('click', (event) => {
        console.log('Map clicked at:', event.latLng);

        placeMarker(event.latLng);
        fetchPlaceDetails(event.latLng); // Generowanie linku dla pinezki
    });

    const input = document.createElement('input');
    input.id = 'searchInput';
    input.type = 'text';
    input.placeholder = 'Wyszukaj miejsce';

    map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);

    autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    autocomplete.addListener('place_changed', () => {
        const place = autocomplete.getPlace();
        console.log('Place selected:', place);

        if (!place.geometry || !place.geometry.location) {
            console.error('Place has no geometry or location.');
            window.alert("Nie znaleziono miejsca");
            return;
        }

        placeMarker(place.geometry.location);
        map.setCenter(place.geometry.location);
        map.setZoom(15);

        document.getElementById('latitude').value = place.geometry.location.lat();
        document.getElementById('longitude').value = place.geometry.location.lng();
        document.getElementById('place_name').value = place.name;
        document.getElementById('location_url').value = `https://www.google.com/maps/place/?q=place_id:${place.place_id}`;
    });
}

function placeMarker(location) {
    console.log('Placing marker at:', location);

    if (marker) {
        marker.setPosition(location);
    } else {
        marker = new google.maps.Marker({
            position: location,
            map: map
        });
    }

    document.getElementById('latitude').value = location.lat();
    document.getElementById('longitude').value = location.lng();
}

function fetchPlaceDetails(location) {
    const geocoder = new google.maps.Geocoder();

    geocoder.geocode({ location }, (results, status) => {
        console.log('Geocoding input:', location);

        if (status === 'OK' && results.length > 0) {
            const relevantResult = results.find(result =>
                result.types.includes('street_address') ||
                result.types.includes('route')
            ) || results[0];

            console.log('Relevant geocoding result:', relevantResult);
//



            let placeUrl = '';
            let placeUrl = '';
            if (relevantResult.plus_code) {
                // Priorytetowo traktujemy Plus Code
                console.log('Using Plus Code:', relevantResult.plus_code.global_code);
                placeUrl = `https://www.google.com/maps?q=${relevantResult.plus_code.global_code}`;
            } else if (relevantResult.place_id) {
                placeUrl = `https://www.google.com/maps/place/?q=place_id:${relevantResult.place_id}`;

//            if (relevantResult.place_id) {
//                placeUrl = `https://www.google.com/maps/place/?q=place_id:${relevantResult.place_id}`;
//            } else if (relevantResult.plus_code) {
//                // Obsługuje sytuację, gdy zwrócony wynik to Plus Code
//                console.log('Using Plus Code:', relevantResult.plus_code.global_code);
//                placeUrl = `https://www.google.com/maps?q=${relevantResult.plus_code.global_code}`;
            } else {
                placeUrl = `https://www.google.com/maps?q=${location.lat()},${location.lng()}`;
            }

            document.getElementById('place_name').value = relevantResult.formatted_address || 'Brak danych';
            document.getElementById('location_url').value = placeUrl;

            console.log('Generated URL:', placeUrl);
        } else {
            console.error('Geocoding failed or returned no results:', status);

            const fallbackUrl = `https://www.google.com/maps?q=${location.lat()},${location.lng()}`;
            document.getElementById('place_name').value = 'Nieznane miejsce';
            document.getElementById('location_url').value = fallbackUrl;

            console.log('Fallback URL:', fallbackUrl);
        }
    });
}

//            const placeId = relevantResult.place_id;
//            const placeUrl = placeId
//                ? `https://www.google.com/maps/place/?q=place_id:${placeId}`
//                : `https://www.google.com/maps?q=${location.lat()},${location.lng()}`;
//
//            document.getElementById('place_name').value = relevantResult.formatted_address || 'Brak danych';
//            document.getElementById('location_url').value = placeUrl;
//
//            console.log('Generated URL:', placeUrl);
//        } else {
//            console.error('Geocoding failed or returned no results:', status);
//
//            const fallbackUrl = `https://www.google.com/maps?q=${location.lat()},${location.lng()}`;
//            document.getElementById('place_name').value = 'Nieznane miejsce';
//            document.getElementById('location_url').value = fallbackUrl;
//
//            console.log('Fallback URL:', fallbackUrl);
//        }
//    });
//}
