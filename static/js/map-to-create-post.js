let map, marker, autocomplete;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 12.4634, lng: 53.8232 },  // Domyślne centrum (możesz zmienić)
        zoom: 8
    });


    map.addListener('click', (event) => {
    placeMarker(event.latLng);
    fetchPlaceDetails(event.latLng); // To zapewnia generowanie linku dla pinezki
});

    // Utworzenie pola wyszukiwania jako elementu HTML
    const input = document.createElement('input');
    input.id = 'searchInput';
    input.type = 'text';
    input.placeholder = 'Wyszukaj miejsce';

    // Dodanie pola wyszukiwania do mapy jako kontrolki
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);

     // Inicjalizacja autouzupełniania miejsc na podstawie inputu
    autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);  // Związanie autouzupełniania z granicami mapy

    autocomplete.addListener('place_changed', () => {
        const place = autocomplete.getPlace();

        if (!place.geometry || !place.geometry.location) {
            window.alert("Nie znaleziono miejsca");
            return;
        }
//
//    // Inicjalizacja autouzupełniania miejsc
//    const input = document.getElementById('searchInput');
//    autocomplete = new google.maps.places.Autocomplete(input);
//    autocomplete.bindTo('bounds', map);  // Związanie autouzupełniania z granicami mapy
//
//    autocomplete.addListener('place_changed', () => {
//        const place = autocomplete.getPlace();
//
//        if (!place.geometry || !place.geometry.location) {
//            window.alert("Nie znaleziono miejsca");
//            return;
//        }

        // Zaktualizowanie mapy i markera dla wybranego miejsca
        placeMarker(place.geometry.location);
        map.setCenter(place.geometry.location);
        map.setZoom(15);  // Zoom do poziomu detali

        // Ustawianie szczegółów miejsca
        document.getElementById('latitude').value = place.geometry.location.lat();
        document.getElementById('longitude').value = place.geometry.location.lng();
        document.getElementById('place_name').value = place.name;
        document.getElementById('location_url').value = `https://www.google.com/maps/place/?q=place_id:${place.place_id}`;
    });

//
}

function placeMarker(location) {
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

//function fetchPlaceDetails(location) {
//    const geocoder = new google.maps.Geocoder();
//    const service = new google.maps.places.PlacesService(map);
//
//    geocoder.geocode({ 'location': location }, (results, status) => {
//        if (status === 'OK') {
//            if (results[0]) {
//                const placeId = results[0].place_id;
//                const placeUrl = `https://www.google.com/maps/place/?q=place_id:${placeId}`;
//                document.getElementById('location_url').value = placeUrl;
//
//                service.getDetails({ placeId: placeId }, (place, status) => {
//                    if (status === google.maps.places.PlacesServiceStatus.OK) {
//                        document.getElementById('place_name').value = place.name;
//
//                    }
//                });
//            }
//        }
//    });
//}

//function fetchPlaceDetails(location) {
//    const geocoder = new google.maps.Geocoder();
//
//    geocoder.geocode({ 'location': location }, (results, status) => {
//        if (status === 'OK' && results[0]) {
//            const placeId = results[0].place_id;
//            const placeUrl = `https://www.google.com/maps/place/?q=place_id:${placeId}`;
//
//            // Aktualizuj odpowiednie pola
//            document.getElementById('location_url').value = placeUrl;
//            document.getElementById('place_name').value = results[0].formatted_address; // lub inny preferowany format
//        } else {
//            console.error('Nie można pobrać szczegółów miejsca:', status);
//        }
//    });
//}
//function fetchPlaceDetails(location) {
//    const geocoder = new google.maps.Geocoder();
//
//    geocoder.geocode({ 'location': location }, (results, status) => {
//        if (status === 'OK' && results[0]) {
//            const placeId = results[0].place_id;
//            const placeUrl = placeId
//                ? `https://www.google.com/maps/place/?q=place_id:${placeId}`
//                : `https://www.google.com/maps?q=${location.lat()},${location.lng()}`; // Fallback bez place_id
//
//            // Aktualizuj odpowiednie pola
//            document.getElementById('location_url').value = placeUrl;
//            document.getElementById('place_name').value = results[0].formatted_address || 'Brak danych'; // Fallback
//        } else {
//            // Fallback, jeśli geokodowanie się nie powiedzie
//            const fallbackUrl = `https://www.google.com/maps?q=${location.lat()},${location.lng()}`;
//            document.getElementById('location_url').value = fallbackUrl;
//            document.getElementById('place_name').value = 'Nieznane miejsce';
//            console.error('Nie można pobrać szczegółów miejsca:', status);
//        }
//    });
//}
function fetchPlaceDetails(location) {
    const geocoder = new google.maps.Geocoder();

    geocoder.geocode({ 'location': location }, (results, status) => {
        let placeUrl;

        if (status === 'OK' && results[0]) {
            const placeId = results[0].place_id;
            placeUrl = placeId
                ? `https://www.google.com/maps/place/?q=place_id:${placeId}`
                : `https://www.google.com/maps?q=${location.lat()},${location.lng()}`;
            document.getElementById('place_name').value = results[0].formatted_address || 'Brak danych';
        } else {
            placeUrl = `https://www.google.com/maps?q=${location.lat()},${location.lng()}`;
            document.getElementById('place_name').value = 'Nieznane miejsce';
        }

        // Aktualizuj link URL
        document.getElementById('location_url').value = placeUrl;

        // Debugging: Wyświetl dane w konsoli
        console.log('Generated link:', placeUrl);
    });
}
