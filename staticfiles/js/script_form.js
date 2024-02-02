$(document).ready(function () {
    var selectedVehicleType; // Guarda o tipo de veículo selecionado

    // Função para carregar marcas
    function loadBrands(vehicleTypeId) {
        $.ajax({
            url: `/get_brands/${vehicleTypeId}/`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                var brandSelect = $('#id_brand');
                brandSelect.empty().append($('<option>').text('Selecione uma marca'));
                $.each(data, function (index, item) {
                    brandSelect.append($('<option>').val(item.id).text(item.brand));
                });
            },
            error: function (xhr, status, error) {
                console.error('Erro ao carregar marcas:', error);
            }
        });
    }

    function loadYears(modelId) {
        $.ajax({
            url: `/get_years/${modelId}/`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                var yearSelect = $('#id_year');
                yearSelect.empty().append($('<option>').text('Selecione um ano'));
                $.each(data, function (index, item) {
                    yearSelect.append($('<option>').val(item.id).text(item.year));
                });
            },
            error: function (xhr, status, error) {
                console.error('Erro ao carregar anos:', error);
            }
        });
    }

    // Assumindo que o select de modelos tem o id 'id_model'
    $('#id_model').change(function () {
        var modelId = $(this).val();
        if (modelId) {
            loadYears(modelId);
        } else {
            $('#id_year').empty().append($('<option>').text('Selecione um ano'));
        }
    });

    // Função para carregar modelos
    function loadModels(brandId, vehicleTypeId) {
        $.ajax({
            url: `/get_models/${brandId}/${vehicleTypeId}/`,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                var modelSelect = $('#id_model');
                modelSelect.empty().append($('<option>').text('Selecione um modelo'));
                $.each(data, function (index, item) {
                    modelSelect.append($('<option>').val(item.id).text(item.model));
                });
            },
            error: function (xhr, status, error) {
                console.error('Erro ao carregar modelos:', error);
            }
        });
    }

    // Evento de mudança para o tipo de veículo
    $('#id_vehicle_type').change(function () {
        selectedVehicleType = $(this).val();
        loadBrands(selectedVehicleType);
        $('#id_model').empty().append($('<option>').text('Selecione um modelo')); // Limpa os modelos
    });

    // Evento de mudança para a marca
    $('#id_brand').change(function () {
        var selectedBrand = $(this).val();
        if (selectedBrand && selectedVehicleType) {
            loadModels(selectedBrand, selectedVehicleType);
        }
    });

    function loadFuels(yearId) {
    $.ajax({
        url: `/get_fuels/${yearId}/`,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            var fuelSelect = $('#id_fuel');
            fuelSelect.empty().append($('<option>').text('Selecione um combustível'));
            $.each(data, function (index, item) {
                fuelSelect.append($('<option>').val(item.id).text(item.fuel));
            });
        },
        error: function (xhr, status, error) {
            console.error('Erro ao carregar combustíveis:', error);
        }
    });
}

// Evento de mudança para o campo ano
$('#id_year').change(function () {
    var yearId = $(this).val();
    if (yearId) {
        loadFuels(yearId);
    } else {
        $('#id_fuel').empty().append($('<option>').text('Selecione um combustível'));
    }
});
});