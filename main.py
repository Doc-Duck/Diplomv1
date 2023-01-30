from fastapi import FastAPI, APIRouter
from endpoints.specialization import specialization_router
from endpoints.appointments import appointment_router
from endpoints.doctors import doctors_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()
main_api_router = APIRouter()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_api_router.include_router(specialization_router, prefix='/specializations', tags=['Specializations'])
main_api_router.include_router(appointment_router, prefix='/appointments', tags=['Appointments'])
main_api_router.include_router(doctors_router, prefix='/doctors', tags=['Doctors'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)