import { PayloadAction, createSlice } from '@reduxjs/toolkit';
import { ICategory } from '../utils/interfaces/interfaces.ts';

interface IServicesCategoriesState {
  servicesCategories: ICategory[]
}

const initialState: IServicesCategoriesState = {
  servicesCategories: []
}

const servicesCategoriesSlice = createSlice({
  name: 'servicesCategories',
  initialState,
  reducers: {
    addServicesCategories: (state, action: PayloadAction<ICategory[]>) => {
      state.servicesCategories = action.payload;
    }
  }
});

export const { addServicesCategories } = servicesCategoriesSlice.actions;
export const reducer = servicesCategoriesSlice.reducer;
