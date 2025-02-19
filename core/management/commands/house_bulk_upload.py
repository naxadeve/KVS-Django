from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Province, District, HouseHoldData, Municipality

from django.contrib.gis.geos import GEOSGeometry


class Command(BaseCommand):
    help = 'load HouseHold data from .xlsx file'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_excel(path, sheet_name=0)
        upper_range = len(df)

        print("Wait Data is being Loaded")

        for row in range(0, upper_range):
            municipality = Municipality.objects.get(name="Saptakoshi")
            district = municipality.district
            province = district.province

            try:
                house=HouseHoldData.objects.create(
                    # province=Province.objects.get(
                    #     code=(df['Province_id'][row])),
                    #
                    # district=District.objects.get(
                    #     district_code=(df['District_id'][row])),
                    #
                    # name=(df['Name'][row]).capitalize().strip(),
                    #
                    # gn_type_en=(df['Type_en'][row]).capitalize().strip(),
                    #
                    # gn_type_np=(df['Type'][row]).capitalize().strip(),
                    index=df['index'][row],
                    deviceid=df['deviceid'][row],
                    date=df['date'][row],
                    surveyor_name=df['surveyor_name'][row],
                    place_name=df['place_name'][row],
                    province=province,
                    district=district,
                    municipality=municipality,
                    ward=df['ward'][row],
                    house_number=df['house_number'][row],
                    latitude=df['latitude'][row],
                    longitude=df['longitude'][row],
                    altitude=df['altitude'][row],
                    gps_precision=df['gps_precision'][row],
                    household_number=df['household_number'][row],
                    owner_name=df['owner_name'][row],
                    owner_age=df['owner_age'][row],
                    owner_sex=df['owner_sex'][row],
                    owner_status=df['owner_status'][row],
                    owner_status_other=df['owner_status_other'][row],
                    owner_caste=df['owner_caste'][row],
                    owner_caste_other=df['owner_caste_other'][row],
                    religion=df['religion'][row],
                    religion_other=df['religion_other'][row],
                    mother_tongue=df['Mother_tongue'][row],
                    mother_tongue_other=df['mother_tongue_other'][row],
                    contact_no=df['contact_no'][row],
                    owner_education=df['owner_Education'][row],
                    owner_citizenship_no=df['owner_citizenship_no'][row],
                    responder_name=df['responder_name'][row],
                    responder_sex=df['responder_age'][row],
                    responder_contact=df['responder_contact'][row],
                    other_family_living=df['other_families_living'][row],
                    main_occupation=df['Main_occupation'][row],
                    other_occupation=df['other_occupation'][row],
                    business=df['business'][row],
                    other_business=df['other_business'][row],
                    other_small_business=df['other_small_business'][row],
                    crop_sufficiency=df['Crop_sufficiency'][row],
                    food_type=df['food_type'][row],
                    main_staple=df['main_staple'][row],
                    pulses=df['pulses'][row],
                    vegetables=df['vegetables'][row],
                    fruits=df['fruits'][row],
                    meat_and_fish=df['meat_and_fish'][row],
                    milk_and_products=df['milk_and_products'][row],
                    sugar_products=df['sugar_products'][row],
                    oil_products=df['oil_products'][row],
                    condiments=df['condiments'][row],
                    monthly_expenses=df['monthly_expenses'][row],
                    monthly_income=df['monthly_income'][row],
                    loan=df['loan'][row],
                    loan_amount=df['loan_amount'][row],
                    loan_duration=df['loan_duration'][row],
                    animal_presence=df['animal_presence'][row],
                    insurance=df['insurance'][row],
                    other_insurance=df['other_insurance'][row],
                    vehicle=df['Vehicles'][row],
                    vehicles_other=df['vehicles_other'][row],
                    facilities_type=df['facilities_type'][row],
                    other_facilities=df['other_facilities'][row],
                    fuel_type=df['fuel_type'][row],
                    other_fuel_type=df['other_fuel_type'][row],
                    land_ownership=df['land_ownership'][row],
                    house_type=df['house_type'][row],
                    house_type_other=df['house_type_other'][row],
                    house_built_year=df['house_built_year'][row],
                    house_stories=df['house_stories'][row],
                    no_of_rooms=df['no_of_rooms'][row],
                    house_map_registered=df['house_map_registered'][row],
                    building_standard_code=df['building_standard_code'][row],
                    earthquake_resistance=df['earthquake_resistance'][row],
                    flood_prone=df['flood_prone'][row],
                    flood_resilience_activities=df['flood_resilience_activities'][row],
                    flood_activities_resilience_other=df['flood_resilience_activities_other'][row],
                    owned_land_area=df['owned_land_area'][row],
                    owned_land_near_river=df['owned_land_near_river'][row],
                    owned_land_area_near_river=df['owned_land_area_near_river'][row],
                    owned_land_image_name=df['owned_land_image'][row],
                    technical_manpower_presence=df['technical_manpower_presence'][row],
                    manpower_type=df['manpower_type'][row],
                    doctor_sex=df['doctor_sex'][row],
                    doctor_male_number=df['doctor_male_number'][row],
                    doctor_female_number=df['doctor_female_number'][row],
                    engineer_sex=df['engineer_sex'][row],
                    engineer_male_number=df['engineer_male_number'][row],
                    engineer_female_number=df['engineer_female_number'][row],
                    subengineer_sex=df['subengineer_sex'][row],
                    subengineer_male=df['subengineer_male_number'][row],
                    subengineer_female=df['subengineer_female_number'][row],
                    nurse_sex=df['nurse_sex'][row],
                    nurse_male_number=df['nurse_male_number'][row],
                    nurse_female_number=df['nurse_female_number'][row],
                    ha_lab_sex=df['ha_lab_sex'][row],
                    ha_lab_male_number=df['ha_lab_male_number'][row],
                    ha_lab_female_number=df['ha_lab_female_number'][row],
                    veterinary_sex=df['veterinary_sex'][row],
                    veterinary_male_number=df['veterinary_male_number'][row],
                    veterinary_female_number=df['veterinary_female_number'][row],
                    dakarmi_sikarmi_sex=df['dakarmi_sikarmi_sex'][row],
                    dakarmi_sikarmi_male_number=df['dakarmi_sikarmi_male_number'][row],
                    dakarmi_sikarmi_female_number=df['dakarmi_sikarmi_female_number'][row],
                    plumber_sex=df['plumber_sex'][row],
                    plumber_male_number=df['plumber_male_number'][row],
                    plumber_female_number=df['plumber_female_number'][row],
                    electrician_sex=df['electrician_sex'][row],
                    electrician_male_number=df['electrician_male_number'][row],
                    electrician_female_number=df['electrician_female_number'][row],
                    jt_sex=df['jt_sex'][row],
                    jt_male_number=df['jt_sex'][row],
                    jt_female_number=df['jt_sex'][row],
                    other_technical=df['other_technical'][row],
                    other_technical_sex=df['other_technical_sex'][row],
                    other_technical_male_number=df['other_technical_male_number'][row],
                    other_technical_female_number=df['other_technical_female_number'][row],
                    distance_from_main_road=df['distance_from_main_road'][row],
                    road_type=df['road_type'][row],
                    road_width=df['road_width'][row],
                    road_capacity=df['road_capacity'][row],
                    distance_from_nearest_school=df['distance_from_nearest_school'][row],
                    distance_from_nearest_health_institution=df['distance_from_nearest_health_institution'][row],
                    distance_from_nearest_security_forces=df['distance_from_nearest_security_forces'][row],
                    water_sources=df['water_sources'][row],
                    water_sources_other=df['water_sources_other'][row],
                    tubewell_type=df['tubewell_type'][row],
                    tubewell_status=df['tubewell_status'][row],
                    no_of_houses_using_tubewell=df['no_of_houses_using_tubewell'][row],
                    has_flood_effect_tubewell=df['has_flood_affected_tubewell'][row],
                    public_tap_distance=df['public_tap_distance'][row],
                    toilet_facility=df['toilet_facility'][row],
                    toilet_type=df['toilet_type'][row],
                    toilet_type_other=df['toilet_type_other'][row],
                    waterborne_disease=df['waterborne_disease'][row],
                    disaster_type=df['disaster_type'][row],
                    disaster_type_other=df['disaster_type_other'][row],
                    hazard_type=df['hazard_type'][row],
                    hazard_type_other=df['hazard_type'][row],
                    is_there_identified_risk_areas=df['is_there_identified_risk_areas'][row],
                    disaster_information_medium=df['disaster_information_medium'][row],
                    disaster_information_medium_other=df['disaster_information_medium_other'][row],
                    knowledge_on_early_warning_system=df['knowledge_on_early_warning_system'][row],
                    early_warning_system_installed_nearby=df['early_warning_system_installed_nearby'][row],
                    got_early_warning_during_disaster=df['got_early_warning_during_disaster'][row],
                    got_early_warning_during_through=df['got_early_warning_through'][row],
                    medium_suitable_for_early_warning=df['medium_suitable_for_early_warning'][row],
                    other_medium_suitable_for_early_warning=df['other_medium_suitable_for_early_warning'][row],
                    evacuation_shelter_availability=df['evacuation_shelter_availability'][row],
                    distance_to_evacuation_shelter=df['distance_to_evacuation_shelter'][row],
                    capacity_of_evacuation_shelter=df['capacity_of_evacuation_shelter'][row],
                    distance_to_nearest_open_space=df['distance_to_nearest_open_space'][row],
                    distance_to_nearest_market=df['distance_to_nearest_market'][row],
                    goods_available_in_nearest_market=df['goods_available_in_nearest_market'][row],
                    other_goods_available_in_nearest_market=df['other_goods_available_in_nearest_market'][row],
                    distance_to_alternative_market=df['distance_to_alternative_market'][row],
                    alternative_market_name=df['alternative_market_name'][row],
                    nearest_market_operation_during_disaster=df['nearest_market_operation_during_disaster'][row],
                    easy_access_to_goods=df['easy_access_to_goods'][row],
                    how_goods_were_managed_if_not_available_in_market=df['how_goods_were_managed_if_not_available_in_market'][row],
                    warehouse_available_in_ward=df['warehouse_available_in_ward'][row],
                    coping_mechanism_during_disaster=df['coping_mechanism_during_disaster'][row],
                    other_coping_mechanism_during_disaster=df['other_coping_mechanism_during_disaster'][row],
                    emergency_kit_availability_in_house=df['emergency_kit_availability_in_house'][row],
                    emergency_kit_material_update_frequency=df['emergency_kit_material_update_frequency'][row],
                    involved_disaster_training=df['involved_in_disaster_training'][row],
                    involved_disaster_training_type=df['involved_disaster_training_type'][row],
                    involved_disaster_training_type_other=df['involved_disaster_training_type_other'][row],
                    involved_in_simulation_type=df['involved_in_simulation_type'][row],
                    involved_in_simulation_type_other=df['involved_in_simulation_type_other'][row],
                    knowledge_about_ldcrp=df['knowledge_about_ldcrp'][row],
                    involvement_in_ldcrp_development_process=df['involvement_in_ldcrp_development_process'][row],
                    knowledge_about_dprp=df['knowledge_about_dprp'][row],
                    involvement_in_dprp_development_process=df['involvement_in_dprp_development_process'][row],
                    prepared_contingency_plan=df['prepared_contingency_plan'][row],
                    most_occuring_disasters_in_ward=df['most_occuring_disasters_in_ward'][row],
                    identified_safe_place_for_flood=df['identified_safe_place_for_flood'][row],
                    distance_to_safe_place_for_flood=df['distance_to_safe_place_for_flood'][row],
                    damages_occurred_during_flood=df['damages_occured_during_flood'][row],
                    other_damages_occurred_during_flood=df['other_damages_occured_during_flood'][row],
                    house_damage_type_during_flood=df['house_damage_type_during_flood'][row],
                    house_damage_type_during_flood_other=df['house_damage_type_during_flood_other'][row],
                    migrated_place_during_flood=df['migrated_place_during_flood'][row],
                    migrated_place_during_flood_other=df['migrated_place_during_flood_other'][row],
                    damage_occurred_during_landslide=df['damage_occured_during_landslide'][row],
                    other_damage_occurred_during_landslide=df['other_damage_occured_during_landslide'][row],
                    house_damage_type_during_landslide=df['house_damage_type_during_landslide'][row],
                    house_damage_type_during_landslide_other=df['house_damage_type_during_landslide_other'][row],
                    migrated_place_during_landslide=df['migrated_place_during_landslide'][row],
                    damages_occurred_during_earthquake=df['damages_occured_during_earthquake'][row],
                    other_damages_occurred_during_earthquake=df['other_damages_occured_during_earthquake'][row],
                    house_damage_type_during_earthquake=df['house_damage_type_during_earthquake'][row],
                    house_damage_type_during_earthquake_other=df['house_damage_type_during_earthquake_other'][row],
                    migrated_place_during_earthquake=df['migrated_place_during_earthquake'][row],
                    damages_occurred_during_fire=df['damages_occured_during_fire'][row],
                    other_damages_occured_during_fire=df['other_damages_occured_during_fire'][row],
                    house_damage_type_during_fire=df['house_damage_type_during_fire'][row],
                    house_damage_type_during_fire_other=df['house_damage_type_during_fire_other'][row],
                    fire_extinguisher_in_house=df['fire_extinguisher_in_house'][row],
                    migrated_place_during_fire=df['migrated_place_during_fire'][row],
                    migrated_place_during_fire_other=df['migrated_place_during_fire_other'][row],
                    remarks=df['remarks'][row],

                )
                print(row, 'Data was successfully updated')

            except Exception as e:
                print("error in", e)





