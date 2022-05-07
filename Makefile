.PHONY:
api:
	@uvicorn server:app --reload
