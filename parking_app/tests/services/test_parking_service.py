from django.test import TestCase
from unittest.mock import patch, MagicMock
from parking_app.Models.parking_model import Parking
from parking_app.services.parking_service import ParkingService
from parking_app.Enums.parking_status import ParkingStatus
class TestParkingService(TestCase):

    @patch('parking_app.services.parking_service.ScheduleService')
    @patch('parking_app.services.parking_service.LocationService')
    def setUp(self, mock_location_service, mock_schedule_service):
        self.parking_service = ParkingService()
        self.mock_location_service = mock_location_service.return_value
        self.mock_schedule_service = mock_schedule_service.return_value

    def test_get_parkings(self):
        # Simular una lista de parkings
        mock_parkings = [Parking(id=1, owner_id='1', description='Parking 1')]
        # Mockear el método all() de Parking.objects
        with patch.object(Parking.objects, 'all', return_value=mock_parkings):
            result = self.parking_service.get_parkings()
            self.assertEqual(result, mock_parkings)

    def test_create_parking(self):
        # Datos de ejemplo para crear un parking
        new_parking_data = {
            'owner_id': '1',
            'description': 'New Parking',
            # Agrega más campos según sea necesario
        }
        # Mockear el método create() de Parking.objects
        with patch.object(Parking.objects, 'create', return_value=Parking(id=1, **new_parking_data)):
            result = self.parking_service.create_parking(new_parking_data)
            self.assertIsNotNone(result)
            self.assertEqual(result['owner_id'], new_parking_data['owner_id'])

    @patch('parking_app.Models.parking_model.Parking.objects.get')
    def test_update_parking_status(self, mock_get):
        # Mock para el objeto Parking
        mock_parking = Parking(id=1, name='Parking 1', owner_id='1', state=ParkingStatus.AVAILABLE)
        mock_get.return_value = mock_parking

        # Estado nuevo para actualizar
        new_status = ParkingStatus.OCCUPIED

        # Llamar al método que se está probando
        result = self.parking_service.update_parking_status(parking_id=1, status=new_status)

        # Verificar que el objeto Parking se actualizó correctamente
        self.assertEqual(result.state, new_status)
        mock_get.assert_called_once_with(id=1)
    # Agrega más pruebas según sea necesario

