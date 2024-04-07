import { IServiceExtended, IServiceCategory } from '../utils/interfaces/interfaces.ts';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface IAvailableServicesState {
  availableServices: IServiceExtended[],
  categorizedServices: IServiceCategory[],
  popularServices: IServiceExtended[],
}

const initialState: IAvailableServicesState = {
  availableServices: [],
  categorizedServices: [],
  popularServices: []
};

const availableServicesSlice = createSlice({
  name: 'availableServices',
  initialState,
  reducers: {
    addAvailableServices: (state, action: PayloadAction<IServiceExtended[]>) => {
      state.availableServices = action.payload;
    },
    addCategorizedServices: (state, action: PayloadAction<IServiceCategory[]>) => {
      state.categorizedServices = action.payload;
    },
    addPopularServices: (state, action: PayloadAction<IServiceExtended[]>) => {
      state.popularServices = action.payload;
    }
  }
});


export const { addAvailableServices, addCategorizedServices, addPopularServices } = availableServicesSlice.actions;
export const reducer = availableServicesSlice.reducer;
